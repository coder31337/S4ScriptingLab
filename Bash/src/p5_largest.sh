LARGEST=$1
if [ $2 -gt $LARGEST ] ; then
    LARGEST=$2
fi
if [ $3 -gt $LARGEST ] ; then
    LARGEST=$3
fi
echo "Largest number is $LARGEST"
