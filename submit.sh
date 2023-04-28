for mass in 2 5 10 15 20;
do
    for lifetime in 1 10 50 100 500;
    do 
        python histograms_submit_cat1.py -mass ${mass} -lifetime ${lifetime}
    done
done        
