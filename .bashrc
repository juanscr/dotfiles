# ============ PATH CHANGES ============ #
export PATH=$PATH:/usr/local/bin
export PATH=$PATH:/home/juanscr/.bin
export PATH=$PATH:$HOME/src/sfw/MPICH/bin

# ============ ALIASES ============ #
# ==== Files ==== #
alias cgfi="emacs ~/.config/i3/config"

# ==== Commands ==== #
alias e="emacs"

alias lmk="latexmk -pdf"

alias sudo="sudo "

alias ll='ls -alF'
alias la='ls -A'

# ==== Coloring ==== #
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# ==== XDG Compliance ==== #
alias nvidia-settings="nvidia-settings --config="$XDG_CONFIG_HOME"/nvidia/settings"
alias wget='wget --hsts-file="$XDG_CACHE_HOME/wget-hsts"'

# ==== Git ==== #
alias dfiles='/usr/bin/git --git-dir=$HOME/juanscr/dotfiles --work-tree=$HOME'

function gitd() {
  if ! git rev-parse --git-dir &>/dev/null
  then
    dfiles "$@"
  else
    git "$@"
  fi
}
function pullCheck() {
  branch=$(gitd branch -l | awk '/^\*.*/{ print $2 }')
  gitd checkout $1 && gitd pull && gitd checkout $branch
}
alias ga='gitd add'
alias gc='gitd checkout'
alias gca='gitd commit -a'
alias gcm='gitd commit -m'
alias gd='gitd diff'
alias gp='gitd push'
alias gpc='pullCheck '
alias gpl='gitd pull'
alias gs='gitd status'

# ==== Global Variables ==== #
export BROWSER="/usr/bin/brave-browser"

# GHCup installation
[ -f "${GHCUP_INSTALL_BASE_PREFIX:=$HOME}/.ghcup/env" ] && \
source "${GHCUP_INSTALL_BASE_PREFIX:=$HOME}/.ghcup/env"

# ============ BASH Terminal ============ #
# ==== Prompt ==== #
# Chroot standard command
PS1="${debian_chroot:+($debian_chroot)}"

# User and git
PS1+="[\[\033[01;32m\]\u\$(__git_ps1 '(%s)')\[\033[00m\] "

# Working directory
PS1+="\[\033[01;34m\]\W\[\033[00m\]] "

# Necessary for git_ps1 to work
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

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


