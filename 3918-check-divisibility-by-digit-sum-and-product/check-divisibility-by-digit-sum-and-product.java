class Solution {
    public boolean checkDivisibility(int n) {
        int m = n;
        ArrayList <Integer> lst = new ArrayList<>();
        while(n>0){
            if(n==0){
                break;
            }
            else{
                lst.add(n%10);
                n=(n-(n%10))/10;
            }
        }
        int sum=0;
        int pod=1;
        for(int i:lst){
            sum= sum+i;
            pod= pod*i;

        }
        if (m%(sum+pod)==0){
            return true;
        }
        return false;
        
    }
}