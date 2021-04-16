# ============ PATH CHANGES ============ #
export PATH=$PATH:/usr/local/bin
export PATH=$PATH:$HOME/.bin
export PATH=$PATH:$HOME/.cabal/bin
export PATH=$PATH:$HOME/.local/bin

# ============ ALIASES ============ #
alias e="emacsclient -n -c"

# Latex
alias lmk="latexmk -pdf"
alias lmks="lmk -shell-escape"

files_to_keep=".*\.\(tex\|sty\|bst\|bib\|cls\)$"
alias rmtrash='find . -maxdepth 1 -type f ! -regex "$files_to_keep" -delete'

# Allows for using alias with sudo
alias sudo="sudo "

# Edit files with sudo privileges
alias se='SUDO_EDITOR="emacsclient -c" sudoedit'

# Ls with icons
alias ls='ls-icons -v'
alias ll='ls -alF'
alias la='ls -A'

# Haskell with dynamic linking
alias ci='cabal install --ghc-options=-dynamic'
alias gfl='ghc -dynamic -Wall -Wmissing-signatures -Wmissing-local-signatures'
alias hdoc='haddock --optghc=-dynamic --html -o doc'

# Autoremove equivalent
alias autoremove='pacman -Qtdq | sudo pacman -Rns -'

# Image display with kittens
alias icat='kitty +kitten icat'

# Compression related commands
alias comp='arc archive'
alias unco='arc unarchive'

# Whatsapp
whatsapp1='nativefier web.whatsapp.com --name whatsapp --single-instance'
whatsapp2='--tray --inject whatsapp-assets/whatsapp-nativefier-inject.js'
whatsapp3='--icon whatsapp-assets/icon.png'
alias genw='$whatsapp1 $whatsapp2 $whatsapp3'

# Spotify terminal user interface
alias lspt='$HOME/.bin/launchspt.sh'
alias cspt='killall spotifyd'

# Okular theming
alias okular='QT_STYLE_OVERRIDE=adwaita-dark QT_QPA_PLATFORMTHEME=gtk3 okular'

# Movies related stuffs
alias movie-mode='xset s off -dpms'

# Update python
awkCom="{ match (\$0, \".*==\", a); gsub (\"=\", \"\", a[0]); print a[0] }"
alias uppy="pip list --outdated --format=freeze | $awkCom | xargs -n1 pip install"

# ==== Coloring ==== #
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

# ==== XDG Compliance ==== #
alias wget='wget --hsts-file="$XDG_CACHE_HOME/wget-hsts"'

# ==== Git ==== #
# Command for adding all passwords
alias pwg='eval `ssh-agent` && ssh-add'

alias dfiles='/usr/bin/git --git-dir=$HOME/juanscr/dotfiles --work-tree=$HOME'

# Function which calls git, if inside a repository or my dotfiles alias
# otherwise.
function gitd() {
  if ! git rev-parse --git-dir &>/dev/null
  then
    dfiles "$@"
  else
    git "$@"
  fi
}

# Function that pulls an specific branch from git.
function pullCheck() {
  branch=$(gitd branch -l | awk '/^\*.*/{ print $2 }')
  gitd checkout $1 && gitd pull
  gitd checkout $branch &>/dev/null
}

alias ga='gitd add'
alias gb='gitd branch'
alias gc='gitd checkout'
alias gca='gitd commit -a'
alias gcl='git clone'
alias gcm='gitd commit -m'
alias gd='gitd diff'
alias gp='gitd push'
alias gpc='pullCheck '
alias gpl='gitd pull'
alias gr='gitd rm'
alias grs='gitd restore --staged'
alias gs='gitd status'

# Generate video of commits
flags1='--auto-skip-seconds 1 --file-idle-time 0 --seconds-per-day 1'
flags2='-y -r 60 -f image2pipe -vcodec ppm -i - -vcodec libx264'
flags3='-preset ultrafast -pix_fmt yuv420p -crf 1 -threads 0 -bf 0'
alias gitvideo='gource $flags1 -1920x1080 -o - | ffmpeg $flags2 $flags3'

# ==== Global Variables ==== #
export BROWSER="/usr/bin/firefox"

# Fraudsim
source /home/juanscr/.bin/private/fraudsim.sh

# ============ BASH Terminal ============ #
# ==== Minimalist Prompt ==== #
# Colors
GREEN="\[\e[01;32m\]"
BLUE="\[\e[01;34m\]"
RESET="\[\e[00m\]"

# Chroot standard command
PS1="${debian_chroot:+($debian_chroot)}"

# Git branch
source /usr/share/git/completion/git-prompt.sh
PS1+="${GREEN}\$(__git_ps1 '(%s) ')${RESET}"

# Working directory
PS1+="${BLUE}\W${RESET} > "

# ==== Keybindings ==== #
bind '"\ew": forward-word'
bind '"\eb": backward-word'
bind '"\eh": backward-char'
bind '"\el": forward-char'
bind '"\e$": end-of-line'
bind '"\e0": beginning-of-line'

bind '"\en": next-history'
bind '"\ep": previous-history'

# ==== History settings ==== #
HISTSIZE=1000
HISTFILESIZE=2000
shopt -s histappend
HISTCONTROL=ignoreboth

# ==== Resizing ==== #
shopt -s checkwinsize
