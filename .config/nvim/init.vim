" Default recommended settings
set nocompatible              " be iMproved, required
filetype off                  " required

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
set number

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
