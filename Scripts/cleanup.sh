for dir in ./*; do
    [ "$dir" = ".venv" ] && continue
    #rm -rf "$dir"
    echo $dir
done