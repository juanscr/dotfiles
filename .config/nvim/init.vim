" Default recommended settings
set nocompatible
filetype off

"""""""""""""""""""""""""""""
" Color scheme
"""""""""""""""""""""""""""""
" Use 256 colors
set t_Co=256

" Correctly load theme
set termguicolors

" Dracula theme package
packadd! dracula
syntax enable
colorscheme dracula

"""""""""""""""""""""""""""""
" Statusline
"""""""""""""""""""""""""""""
packadd! lightline
let g:lightline = { 'colorscheme': 'darcula', }

"""""""""""""""""""""""""""""
" Editor settings
"""""""""""""""""""""""""""""
" Tab settings
set expandtab
set smarttab
set shiftwidth=4
set tabstop=4

" Copy and paste using system clipboard
set clipboard+=unnamedplus

" Show number lines
set number

"""""""" Trailing white space
" Remove TWS function
function TrimWhiteSpace()
  %s/\s*$//
  ''
endfunction

" Remove TWS after saving
autocmd BufWritePre * call TrimWhiteSpace()

" Highlight TWS
highlight RedundantSpaces ctermbg=red guibg=red
match RedundantSpaces /\s\+$/
