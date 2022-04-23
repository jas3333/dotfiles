source $HOME/.config/nvim/plug-config/coc.vim




call plug#begin('~/.config/nvim/plugins')

Plug 'neoclide/coc.nvim',{'branch':'release'}
Plug 'jiangmiao/auto-pairs'
Plug 'machakann/vim-sandwich'
Plug 'preservim/nerdcommenter'
Plug 'preservim/nerdtree'
Plug 'morhetz/gruvbox'
"Plug 'dylanaraps/wal.vim'
call plug#end()



" Keybinds
let g:mapleader=","
nnoremap <tab> gt 
imap jj <Esc>


" Window splitting/movement
function! WinMove(key)
    let t:curwin = winnr()
    exec "wincmd ".a:key
    if (t:curwin == winnr())
        if (match(a:key,'[jk]'))
            wincmd v
        else
            wincmd s
        endif
        exec "wincmd ".a:key
    endif
endfunction

nnoremap <silent> <C-h> :call WinMove('h')<CR>
nnoremap <silent> <C-j> :call WinMove('j')<CR>
nnoremap <silent> <C-k> :call WinMove('k')<CR>
nnoremap <silent> <C-l> :call WinMove('l')<CR>


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
set rulerformat=%15(%c%V\ %p%%%)
set ruler
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

" Ignore case in search
set ignorecase

set showmatch

" Highlights search while typing
set incsearch

" Highlights search
set hlsearch



" Set theme
"colorscheme wal
"
let g:gruvbox_transparent_bg = '1'
let g:gruvbox_termcolors = '16'
autocmd VimEnter * ++nested colorscheme gruvbox
" Nodetree keys
nnoremap <f2> :NERDTreeToggle<CR>

nnoremap <C-f> :NERDTreeFind

" Plugins


















