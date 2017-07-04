vector<vector<int> > Solution::prettyPrint(int A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    vector<vector<int>> result;
    
    int max_index = (A * 2) - 2;
    
    for (int i = 0; i <= max_index; ++i) {
        vector<int> row;
        for (int j = 0; j <= max_index; ++j) {
            int new_i = i, new_j = j;
            if (i >= A) {
                new_i = max_index - i;
            } if (j >= A) {
                new_j = max_index - j;
            }
            
            int min_dist;
            if (new_i <= new_j) {
                min_dist = new_i;
            } else {
                min_dist = new_j;
            }
            
            row.push_back(A - min_dist);
        }
        result.push_back(row);
    }
    
    return result;
}
