"""""""""""""""""""""""""""""
" Tab behavior (Change tabs to spaces)
"""""""""""""""""""""""""""""
set expandtab
set smarttab
set shiftwidth=4
set tabstop=4

" Copy and paste using system clipboard
set clipboard+=unnamedplus

" Show number lines
set number number

"""""""""""""""""""""""""""""
" Color scheme dracula
"""""""""""""""""""""""""""""
packadd! dracula
syntax enable
colorscheme dracula

"""""""""""""""""""""""""""""
" Statusline
"""""""""""""""""""""""""""""
packadd! lightline
let g:lightline = { 'colorscheme': 'darcula', }
