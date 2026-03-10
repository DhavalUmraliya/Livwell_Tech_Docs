# Monopoly Theme & Visual Assets

The Monopoly module uses a custom color palette and a specific set of visual assets to create a premium gamified experience.

## Color Palette

Defined in `Color` extensions, the Monopoly module uses a sophisticated dark theme with vibrant accents.

| Color Name | Hex Code | Purpose |
| :--- | :--- | :--- |
| **`monopolyBg`** | `#201E1F` | Main screen background. |
| **`monopolyPrimary`** | `#F03457` | Primary action buttons and highlights. |
| **`monopolyCard`** | `#DA2128` (25% opacity) | Task and prize card backgrounds. |
| **`monopolyDarkRed`** | `#DA2128` | Secondary accent and floating buttons. |
| **`monopolyTextPrimary`** | `#FDFCFC` | Main body text and titles. |
| **`monopolyTextSecondary`** | `#B1B1B2` | Subtitles and captions. |

## Typography

The module uses the **Manrope** font family for a modern, accessible look.

- **Main Titles**: `.manrope(.bold, size: 20)`
- **Body Text**: `.manrope(.medium, size: 14)`
- **Captions**: `.manrope(.regular, size: 12)`
- **Button Labels**: `.manrope(.semiBold, size: 16)`

## Core Image Assets

- **`FrameDice`**: Static dice image for the idle state.
- **`Dice`**: Large hero asset for the dashboard banner.
- **`bt_grand_prize_icon`**: The bouncing prize box image.
- **`bt_grand_prize_open_icon`**: The revealed prize box image.
- **`giftVector`**: Navigation bar icon for "My Gifts".
- **`gift2`**: Floating gift reveal button asset.
- **`Sunburst`**: Background rays for the prize reveal screen.

## Animations (Lottie & Frame-based)

- **`confity_lottie`**: A Lottie JSON file played on successful prize reveals.
- **Dice Animation**: A sequence of 129 images (`frame_000` to `frame_128`) played manually in `DiceFrameAnimation`.

## UI Components & Design Language

- **Glassmorphism**: Uses dynamic linear gradients and low-opacity fills to create a "glass" effect on cards.
- **Shadows**: Deep shadows (`radius: 12`, `opacity: 0.25`) are used on rules and prize cards for depth.
- **Micro-interactions**: Uses `JelloEffect` (bouncy box) and `rotationEffect` (tilting dice) to make the UI feel alive.
