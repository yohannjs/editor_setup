sudo apt update

# apt packages
sudo apt install vim # Text editor
sudo apt install git # Version control tool
sudo apt install gcc # GNU C Compiler
sudo apt install tmux # Terminal multiplexer
sudo apt install make # Make tool for compiling big software projects
sudo apt install texlive-full # For compiling latex files
sudo apt install python3 # Python 3 interpreter
sudo apt install python3-pip # Python packet manager 
sudo apt install ipython3 # Interactive python environment (for jupyter notebook)
sudo apt install virtualenv # Virtual environment for python programming 
sudo apt install curl # Installer

# Python packages
pip3 install jupyter
pip3 install --user --upgrade pynvim # For vim-autocomplete plugin deoplete

# vim-plug plugin manager for vim
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
