# Flashcard App

A minimal Astro-based flashcard app for studying LeetCode problems.

## Features

- **Set Filtering**: Study all cards, or focus on Set 1 (Recognition) or Set 2 (Mechanics)
- **Flip Cards**: Click "Flip Card" or press Space/Enter to see the answer
- **Navigation**: Use Next/Previous buttons or arrow keys (←/→) or n/p keys
- **Shuffle**: Randomize card order with the shuffle button or 's' key
- **Markdown Support**: Displays formatted markdown content with code syntax highlighting

## Usage

1. Start the development server:
   ```bash
   npm run dev
   ```

2. Open http://localhost:4321 in your browser

3. Use keyboard shortcuts for quick navigation:
   - **Space/Enter**: Flip card
   - **→/n**: Next card
   - **←/p**: Previous card
   - **s**: Shuffle cards
   - **1**: Filter to Set 1 (Recognition)
   - **2**: Filter to Set 2 (Mechanics)
   - **a**: Show all sets

## File Structure

The app automatically loads flashcards from:
- `public/flashcards_set1/` - Recognition flashcards
- `public/flashcards_set2/` - Mechanics flashcards

Each flashcard consists of a front and back markdown file.

## Build for Production

```bash
npm run build
```

The built files will be in the `dist/` directory.