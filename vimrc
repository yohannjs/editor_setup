" Spaces instead of tabs, and tabwidth
set tabstop=4
set shiftwidth=4
set expandtab
" Syntax and colouring
syntax on
colorscheme desert " Different on different computors
" Line numbering (relative except current line)
set nu rnu
" Default is nowrap
set nowrap

"----------- vim-plug plugin manager -----------
" To install plugin manager:
" curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
"     https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
call plug#begin()
Plug 'tpope/vim-sensible'

" On-demand loading
Plug 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle' }

" Autocomplete
" pynvim must be installed for this plugin to work. Please run command below
" before using package.
" pip3 install --user --upgrade pynvim
if has('nvim')
    Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
else
    Plug 'Shougo/deoplete.nvim'
    Plug 'roxma/nvim-yarp'
    Plug 'roxma/vim-hug-neovim-rpc'
endif
let g:deoplete#enable_at_startup = 1
call plug#end()
" To install plugins listed above:
" :PlugInstall
" repo for plugin manager: 
" https://github.com/junegunn/vim-plug
"----------- vim-plug plugin manager -----------
