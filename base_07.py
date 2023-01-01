lass Solution {
public:
    string convertToBase7(int num) 
    {
       string s;
       if (num==0)
       return "0";
        while(num!=0)
        {
            s=to_string(num%7)+s;
            num=num/7;
        }
        string w="";
        w=w+s[0];
        for(int i=1;i<s.size();i++)
        {
            if(s[i]=='-')
            continue;
            else
            w=w+s[i];

        }

        
        return w;
        
    }
};
