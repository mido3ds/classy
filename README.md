# Classy (in construction)

Make c++ classes nicely-formatted, quickly and in an automated way.

Uses special configuration files.

Default formatting style is WebKit, see [WebKit Code Style Guidelines](webkit.org/code-style-guidelines).

Dependencies:

    .Python3.5
    
    .Clang-Format

* Options:


  -h --help: 
        print help.
        
        
  .Files:
  
      -o --out: 
            specify directory to write on (default is CWD).

      -I --include:
            header files to include (inhereted classes will be included automatically).
            
      -C --conf:
            build from configuration file.
            
            
  .Classes:
  
    connect this class with others
  
      --parent: 
            parent class[es] to inherent from.


      --child:
            child classes to build after this (wil be on the same directory).
            all virtual methods will be overriden 

  .Member Type:
  
    methods or attributes (variables).
  
      -m --method:
            class method to add (default to private).


      -a --atr:
            attributes to add (default to private).
            
            
  .Access Modifiers:
  
    add this symbol to member type to specify its accessibility.
    
    ex. -mp read # protected void method `read`
  
  
      -b: public.
      
      -p: private (default).
      
      -r: protected.
      

   .Other:
      
      --style <string>:
        give a style name from the available list.
        
        available formatting styles: [LLVM, Google, Chromium, Mozilla, WebKit (default)].


      -u --using:
        write using namespace <something> as global in the header file.
        
