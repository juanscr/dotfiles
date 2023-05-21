# ============ PATH CHANGES ============ #
export PATH=$PATH:/usr/local/bin
export PATH=$PATH:$HOME/.bin
export PATH=$PATH:$HOME/.cabal/bin
export PATH=$PATH:$HOME/.local/bin

# ============ ALIASES ============ #
# Editor
alias n="nvim"

# Latex
alias lmk="latexmk -pdf"
alias lmks="lmk -shell-escape"

files_to_keep=".*\.\(tex\|sty\|bst\|bib\|cls\)$"
alias rmtrash='find . -maxdepth 1 -type f ! -regex "$files_to_keep" -delete'

# Allows for using alias with sudo
alias sudo="sudo "

# Edit files with sudo privileges
alias se='SUDO_EDITOR="nvim" sudoedit'

# Ls with icons
alias ls='exa --icons --ignore-glob="__pycache__" --group-directories-first'
alias la='exa --icons --group-directories-first -lah'

# Compression related commands
alias untar='tar xf'

# Spotify terminal user interface
alias lspt='$HOME/.bin/launchspt.sh'
alias cspt='killall spotifyd'

# Movies related stuffs
alias movie-mode='xset s off -dpms'

# Update python
awkCom='{ match ($0, ".*==", a); gsub ("=", "", a[0]); print a[0] }'
instCom='xargs -n1 pip install --upgrade'
alias uppy='pip list --outdated --format=freeze | awk "$awkCom" | $instCom'

# ==== Coloring ==== #
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

# ==== XDG Compliance ==== #
alias wget='wget --hsts-file="$XDG_CACHE_HOME/wget-hsts"'

# ==== Git ==== #
# Command for adding all passwords
alias pwg='eval `ssh-agent` && ssh-add'

alias dfiles='/usr/bin/git --git-dir=$HOME/external/dotfiles --work-tree=$HOME'

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
export npm_config_prefix="$HOME/.local"

# ============ BASH Terminal ============ #
# ==== Minimalist Prompt ==== #
# Colors
GREEN="\[\e[01;32m\]"
BLUE="\[\e[01;34m\]"
RESET="\[\e[00m\]"

# Chroot standard command
PS1="${debian_chroot:+($debian_chroot)}"

# Git branch
source /usr/share/git-core/contrib/completion/git-prompt.sh
PS1+="${GREEN}\$(__git_ps1 '(%s) ')${RESET}"

# Working directory
PS1+="${BLUE}\W${RESET} > "

# ==== Keybindings ==== #
# Function for interactive shell
function is_interactive_shell() {
  [[ "$-" =~ "i" ]]
}

# Fix for root bind warning
# http://gurdiga.com/blog/2018/04/14/bind-warning-line-editing-not-enabled/
if is_interactive_shell; then
  bind '"\ew": forward-word'
  bind '"\eb": backward-word'
  bind '"\eh": backward-char'
  bind '"\el": forward-char'
  bind '"\e$": end-of-line'
  bind '"\e0": beginning-of-line'

  bind '"\en": next-history'
  bind '"\ep": previous-history'
fi

# ==== History settings ==== #
HISTSIZE=1000
HISTFILESIZE=2000
shopt -s histappend
HISTCONTROL=ignoreboth

# ==== Resizing ==== #
shopt -s checkwinsize

if ! pgrep -u "$USER" ssh-agent > /dev/null; then
    ssh-agent -t 1h > "$XDG_RUNTIME_DIR/ssh-agent.env"
fi
if [[ ! "$SSH_AUTH_SOCK" ]]; then
    source "$XDG_RUNTIME_DIR/ssh-agent.env" >/dev/null
fi
ssh-add ~/.ssh/id_rsa1 2>/dev/null
ssh-add 2>/dev/null
