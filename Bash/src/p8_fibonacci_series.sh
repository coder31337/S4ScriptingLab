read -p "Enter limit: " N
A=0
B=1
echo "The fibonacci series is "
echo "$A"
echo "$B"
for (( i=0; i<N-2; i++ )) ; do
    F=$((A+B))
    echo "$F"
    A=$B
    B=$F
done
