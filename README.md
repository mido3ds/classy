# Classy #

> Make c++ classes nicely-formatted, quickly and in an automated way.
>
> Runs from the command line or reads special configuration files.
>
> Default formatting style is webkit, see [webkit Code Style Guidelines](webkit.org/code-style-guidelines).


## Dependencies:
    .Python3.5

    .Clang-Format


## Options:

  1. Access Modifiers:
  
    ex. -p '`void read()`' # protected void method read
  

      -b: public.
      
      -p: private.
      
      -r: protected.
        

  2. Files:

    directories and header files  

      -o --out: 
            specify directory to write on (default is CWD).

      -I --include:
            header files to include (inhereted classes will be included automatically).
            
      -C --conf:
            build from configuration file.
            
            
  3. Classes:
  
    connect this class with others

  
      --parent: 
            parent class[es] to inherent from.


      --child:
            child classes to build after this (wil be on the same directory).
            all virtual methods will be overriden 

      
   4. Other:

     misc.

      
      --style <string>:
        give a style name from the available list.

        available formatting styles: [llvm, google, chromium, mozilla, webkit (default)].


      -u --using:
         write using namespace <something> as global in the header file.
        
