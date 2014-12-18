" Sending selected code to Maya
" Last Change:	2014 Dec 16
" Maintainer:	Michitaka Inoue
" License:	This vim script is placed in the public domain.
"
" References
" https://gist.github.com/float1251/fdad4eae7644a5f5eb4e
" http://nanasi.jp/articles/code/screen/visual.html

if exists("g:loaded_vtom")
  finish
endif
let g:loaded_typecorr = 1

let s:save_cpo = &cpo
set cpo&vim

let $VIMTOMAYA_LOCATION = expand('<sfile>:p:h')
autocmd BufNewFile,BufRead,BufEnter *.py let s:vtom_fileType = "python"
autocmd BufNewFile,BufRead,BufEnter, *.mel let s:vtom_fileType = "mel"

function! RunMayaPython()
  python << EOF
import vim, sys
if vim.eval("$VIMTOMAYA_LOCATION") in sys.path:
    pass
else:
    sys.path.append(vim.eval("$VIMTOMAYA_LOCATION"))
import vtom
reload(vtom)
vm = vtom.VimToMaya(vim.eval("$VIMTOMAYA_LOCATION"), vim.eval("s:vtom_fileType"))
vm.run()
EOF
endfunction

function! SendToMaya() range
  let tmp = @@
  silent normal gvy
  let selected = @@
  let @@ = tmp
  try
    '<,'>w! $VIMTOMAYA_LOCATION/tmpScript.py
  catch
    echo "Failed to save tmp file"
  endtry
  try
    call RunMayaPython()
  catch
    echo "failed to run python script"
  endtry
endfunction

let &cpo = s:save_cpo
