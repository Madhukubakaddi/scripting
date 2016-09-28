#!/tools/bin/bash

echo "SDK_PATH:$SDK"
cd $SDK

if false ; then
# Check if the number of arguments($#) passed is nil
if [ $# -eq 0 ]
then        
  git pull &
  echo "$?:Master branch checkout successfully"
elif [ $# -eq 1 ]; then  # To add "then" on the same line prefix with it with ";"
  git checkout $1 & 
  echo "$1 branch checkout successfull"
else 
  echo "Error:$0 needs single branch to checkout"
# "exit 1" returns the exit status of the script as "1" "
  exit 1
fi

# "$!" gives the last proccess id
PID=$!

# wait until the last process is complete
wait $PID

# Check if the exit status($?) of the last executed command
if [ $? -eq 0 ] 
then
   echo "Building code browser"
   browser
   find . -name "*.c" -o -name "*.cpp" -o -name "*.cc" -o -name "*.h" -o -name "*.hpp" > cscope.files
   cscope -b -k  -R -I cscope.files
   ctags -L cscope.files
else 
   exit 1
fi  

# Check if the make file already exists
if [ ! -e /make/Make.local ]
then       
   cp $SDK/make/Make.local.template $SDK/make/Make.local
   sed 's/#DEBUG_OPTIMIZE/DEBUG_OPTIMIZE/' make/Make.local > temp_make
   mv temp_make make/Make.local
fi

# Reading user input with "read"
echo "Enter the processor to build image and press ENTER"
echo -e "*gto\n*iproc\n*sim\n*none"
read image

# String comparison
if [ "$image" == "sim" ]
then
   echo "Building BCM simulator"
   cd $SDK/systems/sim/
   make -s
elif [ "$image" == "gto" ]   
then
   echo "Building GTO image"
   cd $SDK/systems/linux/user/gto
   make -s
elif [ "$image" == "iproc"] 
then
   echo "Building GTO image"
   cd $SDK/systems/linux/user/iproc-3_6
   make -s   
fi   
fi

## The function has be declared before it can be used
browser () {
# Accessing arguments passed to the function
        echo "hello : $1"
}

browser param

## Reading text line by line from file, -r option does not treat backslashes in file as special charater
## line is a variable name. Can be anything
while read -r line
do 
        echo "$line"
done < /home/madhuku/AE/mirror_egr_ing_true  # Can give absolute path, relative path or argument with filename($file)

exit 0
