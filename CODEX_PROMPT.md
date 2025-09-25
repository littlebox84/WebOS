# WebOS - Complete Implementation Prompt for Codex

## 🎯 Project Overview
Create a fully functional, browser-based operating system called **WebOS** that operates as a single HTML file. This must be a complete, working system with actual functionality, not UI mockups.

## 🔧 Technical Requirements
- **Single HTML file** - All CSS, JavaScript, and assets inline
- **Fully functional applications** - Each app must actually work
- **File system with persistence** - Save/load files using localStorage
- **Real window management** - Actual drag, resize, minimize, maximize
- **Working terminal** - Execute real commands
- **Functional calculator** - Perform actual calculations
- **Real web browser** - Navigate to actual websites
- **Working text editor** - Create, edit, save text files
- **File explorer** - Browse actual file system
- **Media player** - Play actual audio/video files
- **Image viewer** - Display actual images
- **Settings** - Actually change system preferences

## 📱 Complete Application Suite

### 1. File Explorer++ (WORKING)
- **Real file system** using localStorage
- **Create, rename, delete files and folders**
- **Navigate directory structure**
- **File operations**: copy, cut, paste, move
- **File previews** for text, images
- **Search functionality**
- **Drag and drop file upload**

### 2. Web Browser (WORKING)
- **Navigate to actual websites** using iframe
- **Address bar with URL input**
- **Back/forward navigation**
- **Refresh functionality**
- **Bookmark system** with persistence
- **Download manager** (simulated)
- **Tab management** (simulated with windows)

### 3. Text Editor (WORKING)
- **Create new text files**
- **Open existing files from file system**
- **Save files to file system**
- **Syntax highlighting** for common languages
- **Find and replace functionality**
- **Multiple encoding support**
- **Print functionality** (browser print)

### 4. Scientific Calculator (WORKING)
- **Basic arithmetic operations** (+, -, *, /)
- **Scientific functions** (sin, cos, tan, log, sqrt)
- **Memory functions** (M+, M-, MR, MC)
- **History tracking** with recall
- **Expression evaluation** with parentheses
- **Keyboard input support**
- **Error handling**

### 5. Terminal Emulator (WORKING)
- **Real command execution**
- **Command history** with arrow keys
- **Tab completion** for commands and files
- **File system commands**: ls, cd, mkdir, rm, cat, touch
- **System commands**: date, clear, help, about, theme
- **Color-coded output**
- **Command piping** (simulated)
- **Environment variables**

### 6. Media Player (WORKING)
- **Play audio files** (MP3, WAV, OGG)
- **Play video files** (MP4, WebM)
- **Playlist management**
- **Volume control**
- **Seek bar** with time display
- **Fullscreen mode**
- **Drag and drop media files**

### 7. Image Viewer (WORKING)
- **Display images** (JPG, PNG, GIF, SVG, WebP)
- **Zoom in/out functionality**
- **Image rotation**
- **Slideshow mode**
- **Image metadata display**
- **Drag and drop image files**
- **Fullscreen viewing**

### 8. System Settings (WORKING)
- **Theme switching** (dark/light/auto)
- **Accent color customization**
- **Font size adjustment**
- **Notification preferences**
- **Auto-save settings**
- **File system reset option**
- **Export/import settings**

## 🎨 Visual Requirements
- **Dark theme** with customizable accent colors
- **Glassmorphism transparency effects**
- **Smooth 60fps animations**
- **Responsive design** for all screen sizes
- **Modern, professional appearance**

## ⚡ System Features
- **Real file system** using localStorage
- **Window management** with drag, resize, minimize, maximize
- **Keyboard shortcuts** (Alt+Tab, Win+D, F11, etc.)
- **Notification system** with actionable toasts
- **Context menus** with right-click functionality
- **PWA support** with offline capability
- **Cross-browser compatibility**
- **Mobile-responsive design**

## 📁 File System Structure
```
/
├── Documents/
│   ├── welcome.txt
│   └── notes/
├── Downloads/
├── Pictures/
├── Music/
├── Desktop/
└── System/
    ├── config.json
    └── bookmarks.json
```

## 🔑 Key Functionalities to Implement

### File System Operations
```javascript
// Create file
webOSFileSystem.createFile('/Documents/newfile.txt', 'content');

// Create directory
webOSFileSystem.createDirectory('/Documents/Projects');

// Read file
const content = webOSFileSystem.readFile('/Documents/welcome.txt');

// Write file
webOSFileSystem.writeFile('/Documents/notes.txt', 'new content');

// Delete file/directory
webOSFileSystem.delete('/Documents/temp.txt');

// List directory
const files = webOSFileSystem.listDirectory('/Documents');
```

### Application Integration
- **File Explorer** ↔ **Text Editor** (open files)
- **File Explorer** ↔ **Image Viewer** (view images)
- **File Explorer** ↔ **Media Player** (play media)
- **Text Editor** ↔ **File Explorer** (save files)
- **Web Browser** ↔ **File System** (download files)

## 🎯 Implementation Checklist

### ✅ Core System
- [ ] Working file system with localStorage
- [ ] Real window management (drag, resize, minimize, maximize)
- [ ] Notification system
- [ ] Keyboard shortcuts
- [ ] Context menus
- [ ] PWA manifest and service worker

### ✅ Applications
- [ ] File Explorer with full file operations
- [ ] Web Browser with actual navigation
- [ ] Text Editor with save/load functionality
- [ ] Calculator with real calculations
- [ ] Terminal with working commands
- [ ] Media Player with file playback
- [ ] Image Viewer with image display
- [ ] Settings with actual configuration changes

### ✅ Advanced Features
- [ ] Drag and drop file upload
- [ ] File system persistence
- [ ] Settings persistence
- [ ] Bookmark system
- [ ] Command history
- [ ] Error handling
- [ ] Performance optimization

## 🚀 Usage Instructions
1. Open `webos.html` in any modern browser
2. All applications are fully functional immediately
3. File system persists between sessions
4. Settings are saved automatically
5. Drag files onto desktop to add them to file system
6. Right-click for context menus
7. Use keyboard shortcuts for power user features

## 🔧 Technical Implementation Notes
- Use `localStorage` for file system persistence
- Use `FileReader` API for file uploads
- Use `Blob` objects for file creation
- Use `URL.createObjectURL()` for media playback
- Use `window.matchMedia()` for theme switching
- Use `navigator.serviceWorker` for PWA functionality

## 📝 Code Structure Requirements
- **Modular design** with clear separation of concerns
- **Extensive commenting** for maintainability
- **Error handling** with user-friendly messages
- **Performance optimization** for 60fps operation
- **Memory management** to prevent leaks
- **Cross-browser compatibility** with fallbacks

This prompt requires creating a complete, working operating system that users can actually use for real tasks, not just a demonstration of UI components.