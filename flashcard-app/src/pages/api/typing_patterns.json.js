import fs from 'fs';
import path from 'path';

export async function GET() {
    try {
        const patternsDir = path.join(process.cwd(), 'public', 'typing-patterns');

        // Check if directory exists
        if (!fs.existsSync(patternsDir)) {
            return new Response(JSON.stringify([]), {
                status: 200,
                headers: { 'Content-Type': 'application/json' }
            });
        }

        // Get all .py files
        const files = fs.readdirSync(patternsDir)
            .filter(f => f.endsWith('.py'));

        // Try to load metadata if it exists
        let customPatterns = {};
        try {
            const metadataPath = path.join(patternsDir, 'patterns.json');
            if (fs.existsSync(metadataPath)) {
                const content = fs.readFileSync(metadataPath, 'utf8');
                const patternsList = JSON.parse(content);
                patternsList.forEach(p => {
                    customPatterns[p.file] = p;
                });
            }
        } catch (e) {
            console.warn('Failed to load patterns.json metadata:', e);
        }

        // Build the response list
        const patterns = files.map(filename => {
            const customInfo = customPatterns[filename];
            const isUnified = filename.startsWith('unified-');

            return {
                filename,
                name: customInfo?.name || formatPatternName(filename),
                isUnified
            };
        });

        // Sort: unified first (alpha), then others (alpha)
        patterns.sort((a, b) => {
            if (a.isUnified && !b.isUnified) return -1;
            if (!a.isUnified && b.isUnified) return 1;
            return a.filename.localeCompare(b.filename);
        });

        return new Response(JSON.stringify(patterns), {
            status: 200,
            headers: {
                'Content-Type': 'application/json'
            }
        });

    } catch (error) {
        console.error('Error scanning typing patterns:', error);
        return new Response(JSON.stringify({ error: 'Failed to scan patterns' }), {
            status: 500,
            headers: {
                'Content-Type': 'application/json'
            }
        });
    }
}

function formatPatternName(filename) {
    return filename
        .replace('.py', '')
        .split('-')
        .map(w => w.charAt(0).toUpperCase() + w.slice(1))
        .join(' ');
}
