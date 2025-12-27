import fs from 'fs';
import path from 'path';

export async function GET() {
  try {
    const publicDir = path.join(process.cwd(), 'public');
    const flashcards = [];

    // Scan all directories in public that start with flashcards_
    const allDirs = fs.readdirSync(publicDir).filter(d => 
      d.startsWith('flashcards_') && 
      fs.statSync(path.join(publicDir, d)).isDirectory()
    );

    for (const setDir of allDirs) {
      const setPath = path.join(publicDir, setDir);
      const files = fs.readdirSync(setPath);
      const frontFiles = files.filter(f => f.endsWith('-front.md'));
      
      // Parse set info from directory name: flashcards_set{N}_{subcategory}
      const parsed = parseSetDir(setDir);
      
      for (const frontFile of frontFiles) {
        const baseName = frontFile.replace('-front.md', '');
        const backFile = `${baseName}-back.md`;
        
        if (files.includes(backFile)) {
          flashcards.push({
            id: `${setDir}-${baseName}`,
            set: setDir,
            setNumber: parsed.setNumber,
            setName: parsed.setName,
            subcategory: parsed.subcategory,
            baseName: baseName,
            frontFile: `/${setDir}/${frontFile}`,
            backFile: `/${setDir}/${backFile}`
          });
        }
      }
    }

    return new Response(JSON.stringify(flashcards), {
      status: 200,
      headers: {
        'Content-Type': 'application/json'
      }
    });
  } catch (error) {
    console.error('Error scanning flashcards:', error);
    return new Response(JSON.stringify({ error: 'Failed to scan flashcards' }), {
      status: 500,
      headers: {
        'Content-Type': 'application/json'
      }
    });
  }
}

function parseSetDir(dirName) {
  // Handle patterns like:
  // flashcards_set0 -> set 0, no subcategory
  // flashcards_set0_time -> set 0, subcategory "time"
  // flashcards_set1_arrays -> set 1, subcategory "arrays"
  
  const match = dirName.match(/^flashcards_set(\d+)(?:_(.+))?$/);
  
  if (!match) {
    return { setNumber: 99, setName: dirName, subcategory: null };
  }
  
  const setNum = parseInt(match[1], 10);
  const subcategory = match[2] || null;
  
  // Special case: set0_space is treated as 0.5 for ordering
  if (setNum === 0 && subcategory === 'space') {
    return { setNumber: 0.5, setName: 'set0', subcategory: 'space' };
  }
  if (setNum === 0 && subcategory === 'time') {
    return { setNumber: 0, setName: 'set0', subcategory: 'time' };
  }
  
  return { 
    setNumber: setNum, 
    setName: `set${setNum}`,
    subcategory: subcategory 
  };
}
