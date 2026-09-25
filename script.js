const term = new Terminal({
    cursorBlink: true,
    theme: {
        background: '#0d0e15',
        foreground: '#f38ba8',
        cursor: '#f5c2e7',
        black: '#45475a',
        red: '#f38ba8',
        green: '#a6e3a1',
        yellow: '#f9e2af',
        blue: '#89b4fa',
        magenta: '#f5c2e7',
        cyan: '#94e2d5',
        white: '#bac2de'
    },
    fontFamily: 'monospace',
    fontSize: 14
});

const fitAddon = new FitAddon.FitAddon();
term.loadAddon(fitAddon);

term.open(document.getElementById('terminal-container'));
fitAddon.fit();

window.addEventListener('resize', () => {
    fitAddon.fit();
});

const prompt = 'fefeh@dev ~ # ';
let currentInput = '';

function runWelcome() {
    term.writeln('\x1b[1;35m:: Arch Linux x86_64 - fefeh.fun TTY\x1b[0m');
    term.writeln('Type \x1b[1;32mhelp\x1b[0m to see available commands.\r\n');
    term.write(prompt);
}

runWelcome();

term.onData(data => {
    const code = data.charCodeAt(0);

    if (code === 13) { // Enter
        term.writeln('');
        handleCommand(currentInput.trim());
        currentInput = '';
        term.write(prompt);
    } else if (code === 127) { // Backspace
        if (currentInput.length > 0) {
            currentInput = currentInput.slice(0, -1);
            term.write('\b \b');
        }
    } else if (code >= 32) { // Printable characters
        currentInput += data;
        term.write(data);
    }
});

function handleCommand(cmd) {
    const args = cmd.split(' ');
    const command = args[0].toLowerCase();

    switch (command) {
        case 'help':
            term.writeln('Available commands:');
            term.writeln('  \x1b[1;32mabout\x1b[0m      - Who is Fefeh?');
            term.writeln('  \x1b[1;32mprojects\x1b[0m   - Check out active projects (StarBot, slovakiamc, etc.)');
            term.writeln('  \x1b[1;32mneofetch\x1b[0m   - System specs');
            term.writeln('  \x1b[1;32mclear\x1b[0m      - Clear screen');
            term.writeln('  \x1b[1;32mcat\x1b[0m        - Usage: cat [file]');
            break;

        case 'about':
            term.writeln('\x1b[1;36m[Bio]\x1b[0m Self-taught developer, system admin, and electronic music producer.');
            term.writeln('Arch Linux user. Reject bloat, embrace CLI.');
            break;

        case 'projects':
            term.writeln('\x1b[1;33mActive Repositories & Infrastructures:\x1b[0m');
            term.writeln('  - StarBot (Discord Bot - discord.js v14)');
            term.writeln('  - slovakiamc.fefeh.fun (Minecraft Survival Server)');
            term.writeln('  - postmarketOS port on Samsung Galaxy J7 Prime');
            break;

        case 'neofetch':
            term.writeln('      /\      \x1b[1;35mfefeh@dev\x1b[0m');
            term.writeln('     /  \\     ---------');
            term.writeln('    /    \\    OS: Arch Linux x86_64');
            term.writeln('   /      \\   Host: Asus VivoBook X543U');
            term.writeln('  /_.--.--._\\  Kernel: Linux 6.x-arch');
            term.writeln('               Uptime: 42 hours, 0 bugs (today)');
            break;

        case 'clear':
            term.clear();
            break;

        case 'cat':
            if (args[1] === 'aboutme.py') {
                term.writeln('# Legacy Python test script - rewritten for the web!');
                term.writeln('print("Hello from fefeh.fun!")');
            } else {
                term.writeln(`cat: ${args[1] || ''}: No such file or directory`);
            }
            break;

        case '':
            break;

        default:
            term.writeln(`zsh: command not found: ${command}`);
            break;
    }
    }
