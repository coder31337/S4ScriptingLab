read -p "Enter limit: " N
A=0
B=1
echo "The fibonacci series is "
echo "$A"
echo "$B"
S=1
for (( i=0; i<N-2; i++ )) ; do
    F=$((A+B))
    echo "$F"
    S=$((S+F))
    A=$B
    B=$F
done
echo "Sum of series is $S"
