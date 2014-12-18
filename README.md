VtoM
====

Send selected code(mel/python) to Maya from Vim.

![](https://dl.dropboxusercontent.com/u/408180/git/images/vtom.gif)

###Install
Copy vtom.vim and vtom.py to `~/.vim/plugin`  
Or if you are using NeoBundle, add the following line to your NeoBundle setting  
`NeoBundle 'minoue/VtoM'`


###Maya
Make sure to open a commandPort as it's written in here.  

[MayaSublime](https://github.com/justinfx/MayaSublime)


###Vim
Select code snippet and run  
`:'<,'>call SendToMaya()`

or  

You can set shortcut key in vimrc to send entire code in one action.  
eg.  
`nnoremap <F5> ggVG:call SendToMaya()<Enter>`
