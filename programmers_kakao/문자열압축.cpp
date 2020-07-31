#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(string s) {
    int answer = 1001;
    if (s.length() == 1)
        return 1;
    for (int i = 1; i <= int(s.length()/2); i++)
    {
        int size = i;
        int start = 0;
        int end = start + size-1;
        int count = 0;
        int combo = 1;
        vector<string> old;
        vector<string> cur;
        for (int j = 0; j <= int(s.length()/size); j++)
        {
            cur.push_back(s.substr(start,size));
            if (old.size() == 0)
                combo = 1;
            else if (!(cur.back() == old.back()))
            {
                if (combo > 1)
                    count += to_string(combo).length();
                count += size;
                combo = 1;
            }
            else
                combo++;
            if (old.size()!=0)
                old.pop_back();
            old.push_back(cur.back());
            cur.pop_back();
            start += size;
            end += size;
        }
        count += s.length()%size;
        answer = min(answer, count);
    }
    return answer;
}