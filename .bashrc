# ============ PATH CHANGES ============ #
export PATH=$PATH:/usr/local/bin
export PATH=$PATH:$HOME/.bin
export PATH=$PATH:$HOME/.cabal/bin
export PATH=$PATH:$HOME/.local/bin

# ============ ALIASES ============ #
# ==== Commands ==== #
alias e="emacsclient -n -c"

# Latex
alias lmk="latexmk -pdf"
alias lmks="lmk -shell-escape"

# Allows for using alias with sudo
alias sudo="sudo "

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

# Tar files
alias tarit='tar -czvf'

# ==== Coloring ==== #
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

# ==== XDG Compliance ==== #
alias wget='wget --hsts-file="$XDG_CACHE_HOME/wget-hsts"'

# ==== Git ==== #
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
alias gc='gitd checkout'
alias gca='gitd commit -a'
alias gcl='git clone'
alias gcm='gitd commit -m'
alias gd='gitd diff'
alias gp='gitd push'
alias gpc='pullCheck '
alias gpl='gitd pull'
alias gr='gitd rm'
alias gs='gitd status'


# ==== Global Variables ==== #
export BROWSER="/usr/bin/firefox"

# QT Style
export QT_STYLE_OVERRIDE=adwaita

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
