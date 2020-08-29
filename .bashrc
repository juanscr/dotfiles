############ PERSONAL COMMANDS ###################
# Path changes
export PATH=$PATH:/usr/local/bin
export PATH=$PATH:/home/juanscr/.bin
export PATH=$PATH:$HOME/src/sfw/MPICH/bin

# Aliases
alias cgfi="emacs ~/.config/i3/config"
alias e="emacs"
alias lmk="latexmk -pdf"
alias sudo="sudo "
alias ll='ls -alF'
alias la='ls -A'

# XDG Directory compliance
alias nvidia-settings="nvidia-settings --config="$XDG_CONFIG_HOME"/nvidia/settings"
alias wget='wget --hsts-file="$XDG_CACHE_HOME/wget-hsts"'

# Dotfiles backup
alias dfiles='/usr/bin/git --git-dir=$HOME/juanscr/dotfiles --work-tree=$HOME'

# Prompt formatting
# Chroot standard command
PS1="${debian_chroot:+($debian_chroot)}"

# User and git
PS1+="[\[\033[01;32m\]\u\$(__git_ps1 '(%s)')\[\033[00m\] "

# Working directory
PS1+="\[\033[01;34m\]\W\[\033[00m\]] "

# Vim-like keybindings
bind '"\ew": forward-word'
bind '"\eb": backward-word'
bind '"\eh": backward-char'
bind '"\el": forward-char'
bind '"\e$": end-of-line'
bind '"\e0": beginning-of-line'

bind '"\en": next-history'
bind '"\ep": previous-history'

# Global Variables
export BROWSER="/usr/bin/brave-browser"

# History settings
HISTSIZE=1000
HISTFILESIZE=2000
shopt -s histappend

# Ignore redundant commands
HISTCONTROL=ignoreboth

# Good behavior when resizing
shopt -s checkwinsize

# GHCup installation
[ -f "${GHCUP_INSTALL_BASE_PREFIX:=$HOME}/.ghcup/env" ] && \
source "${GHCUP_INSTALL_BASE_PREFIX:=$HOME}/.ghcup/env"

# Necessary for git_ps1 to work
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# Coloring of commands
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi
