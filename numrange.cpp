int sum(vector<int> &A, int first, int second) {
    int sum = 0;
    for (int i = first; i < second; ++i) {
        sum += A[i];
    }
    return sum;
}

int Solution::numRange(vector<int> &A, int B, int C) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    int count = 0, first = 0, second = 0;

    for (int i = 0; i < A.size(); ++i) {
        while (i == first || (first != A.size() + 1  && sum(A, i, first) < B)) {
            ++first;
        }
        while (i == second || (second != A.size() + 1 && sum(A, i, second) <= C)) {
            ++second;
        }
        count += (second - first);
    }
    return count;
}
