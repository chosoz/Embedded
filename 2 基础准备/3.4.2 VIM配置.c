"-------------------------------------------------------------------------------  
"           基本设置  
"-------------------------------------------------------------------------------  
" When started as "evim", evim.vim will already have done these settings.  
if v:progname =~? "evim"  
  finish  
endif   
  
"启用Vim的特性，而不是Vi的（必须放到配置的最前边）  
set nocompatible  
  
" 设置编码    
set encoding=utf-8    
set fenc=utf-8    
set fileencodings=ucs-bom,utf-8,cp936,gb2312,gb18030,big5   
   
"显示行号  
set number  
  
"设置默认打开窗口大小  
"set lines=70 columns=100  
  
"设置窗口透明度  
"set transparency=10  
  
"设置背景色  
"set bg=dark  
  
"用 koehler 调色板  
colorscheme koehler  
  
"隐藏工具栏和滑动条  
set guioptions=aAce      
            
"设置标签栏  
"最多30个标签  
set tabpagemax=30   
"显示标签栏    
set showtabline=2     
       
  
"设定文件浏览器目录为当前目录  
"set bsdir=buffer  
"set autochdir  
  
"保存100条命令历史记录  
set history=100   
      
"总是在窗口右下角显示光标的位置  
set ruler     
      
"在Vim窗口右下角显示未完成的命令   
set showcmd           
  
" 启用鼠标  
if has('mouse')  
  set mouse=a  
endif  
  
"设置语法高亮  
if &t_Co > 2 || has("gui_running")  
syntax on  
endif  
  
  
"-------------------------------------------------------------------------------  
"           文本操作设置  
"-------------------------------------------------------------------------------  
"设置字体  
set gfn=Courier:h15  
  
"设置自动缩进  
"设置智能缩进  
set tabstop=4  
set shiftwidth=4  
set softtabstop=4  
set expandtab  
set smarttab  
  
  
"设置Tab键跟行尾符显示出来  
set list lcs=tab:>-,trail:-  
  
"设置自动换行  
set wrap  
  
"设置Insert模式和Normal模式下Left和Right箭头键左右移动可以超出当前行  
set whichwrap=b,s,<,>,[,]  
  
"设置光标移动到屏幕之外时，自动向右滚动10个字符  
set sidescroll=10  
  
"设置使~命令成为操作符命令，从而使~命令可以跟光标移动命令组合使用  
set tildeop  
  
"在Insert模式下，设置Backspace键如何删除光标前边的字符。这里三个值分别表示空白字符，分行符和插入模式之前的字符。  
set backspace=indent,eol,start  
  
"定义键映射，不使用Q命令启动Ex模式，令Q命令完成gq命令的功能---即文本格式化。  
map Q gq  
  
" CTRL-U 在Insert模式下可以删除当前光标所在行所在列之前的所有字符.  Insert模式下，在Enter换行之后，可以立即使用CTRL-U命令删除换行符。  
inoremap <C-U> <C-G>u<C-U>  
  
"使 "p" 命令在Visual模式下用拷贝的字符覆盖被选中的字符。  
vnoremap p <Esc>:let current_reg = @"<CR>gvs<C-R>=current_reg<CR><Esc>  
  
  
"-------------------------------------------------------------------------------  
"           搜索设置  
"-------------------------------------------------------------------------------  
"打开搜索高亮  
set hlsearch  
  
"忽略大小写  
set ignorecase  
  
"在查找时输入字符过程中就高亮显示匹配点。然后回车跳到该匹配点。  
set incsearch     
  
"设置查找到文件尾部后折返开头或查找到开头后折返尾部。  
set wrapscan  
  
  
"put ctrl+shift+- s for find string
nmap <C-_>s :cs find s <C-R>=expand("<cword>")<CR><CR>
nmap <C-_>g :cs find g <C-R>=expand("<cword>")<CR><CR>
nmap <C-_>c :cs find c <C-R>=expand("<cword>")<CR><CR>
nmap <C-_>t :cs find t <C-R>=expand("<cword>")<CR><CR>
nmap <C-_>e :cs find e <C-R>=expand("<cword>")<CR><CR>
nmap <C-_>f :cs find f <C-R>=expand("<cfile>")<CR><CR>
nmap <C-_>i :cs find i ^<C-R>=expand("<cfile>")<CR>$<CR>
nmap <C-_>d :cs find d <C-R>=expand("<cword>")<CR><CR>  
"auto add cscope.out to vim   如:cs f s 命令不能用   
cs add cscope.out
set csto:0
set cscopetag
set nocsverb
set csverb
"添加内核目录，让你在任意文件下搜索时，都能跳到内核信息
"cs add /home/jetbot/kernel/cscope.out  /home/jetbot/kernel/
"set tags:./tags,tags,/home/jetbot/kernel/tags  
  
"-------------------------------------------------------------------------------  
"           文件设置  
"-------------------------------------------------------------------------------  
  
"设置当Vim覆盖一个文件的时候保持一个备份文件，但vms除外（vms会自动备份。备份文件的名称是在原来的文件名上加上 "~" 字符  
if has("vms")  
  set nobackup         
else  
  set backup          
endif  
  
 
"Enter换行时总是使用与前一行的缩进等自动缩进。  
set autoindent  
"设置智能缩进  
set smartindent         
 
  
  
"编辑一个文件时，你所编辑的内容没保存的情况下，可以把现在的文件内容与编辑之前的文件内容进行对比，不同的内容将高亮显示  
if !exists(":DiffOrig")  
  command DiffOrig vert new | set bt=nofile | r ++edit # | 0d_ | diffthis  
          \ | wincmd p | diffthis  
endif  
