VtoM
====

Send selected code to Maya from Vim

![](https://dl.dropboxusercontent.com/u/408180/git/images/vtom.gif)

Open a commandPort as it's written here
[MayaSublime](https://github.com/justinfx/MayaSublime)

Select code snippet and run  
`:'<,'>call SendToMaya()`

or  

Set shortcut key to send entire code in one action.  
eg.  
`nnoremap <F5> ggVG:call SendToMaya()<Enter>`

