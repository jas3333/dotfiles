" Disables compatibility with vi
set nocompatible

" Highlight code syntax
syntax on

" Set tab width to 4 columns
set tabstop=4
set softtabstop=4
set shiftwidth=4

set autoindent

" Use space characters instead of tabs.
set expandtab

" Enable line numbers
set number

" Enable spellcheck
set spell

" Word wrap off
set nowrap

" Highlight cursor line horizontally
" set cursorline

" Auto detect file type
filetype on

" Auto indents based on filetype
filetype indent on

" Enable auto completion menu after hitting tab
set wildmenu

" Make wildmenu run like bash
" set wildmode=list:longest

" Ignore case in search
set ignorecase

set showmatch

" Highlights search while typing
set incsearch

" Highlights search
set hlsearch

" Set theme
set background=dark
let g:gruvbox_contrast_dark='hard' 
colorscheme gruvbox

" Nodetree keys
nnoremap <f2> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind
