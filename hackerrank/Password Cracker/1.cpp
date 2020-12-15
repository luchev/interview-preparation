#include <bits/stdc++.h>
using namespace std;

/**
 * Complexity (n = passwords, k = login attemt)
 * Time complexity: O(n + k)
 * Space complexity: O(n + k)
 */
string passwordCracker(vector<string> passwords, string loginAttempt) {
    set<string> passTable;
    for (auto i : passwords) {
        passTable.insert(i);
    }
    map<string, list<string>> checkedSuffixes;
    list<string> cracked = crackRecursive(passTable, loginAttempt, checkedSuffixes);
    if (cracked.empty()) {
        return "WRONG PASSWORD";
    } else {
        string result;
        for (auto p : cracked) {
            result += p;
            result += " ";
        }
        return rtrim(result);
    }
}

list<string> crackRecursive(set<string> & passTable, string login, map<string, list<string>> & checked) {
    if (login.empty()) {
        list<string> crack;
        crack.push_back(" ");
        return crack;
    }
    if (checked.count(login) == 1) {
        return checked[login];
    }
    string prefix;
    for (int i = 0; i < login.size(); i++) {
        prefix += login[i];
        if (passTable.count(prefix) == 1) {
            list<string> crack = crackRecursive(passTable, login.substr(prefix.size()), checked);
            if (!crack.empty()) {
                crack.push_front(prefix);
                checked[login] = crack;
                return crack;
            }
        }
    }
    checked[login] = list<string>();
    return list<string>();
}

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));
    string t_temp;
    getline(cin, t_temp);
    int t = stoi(ltrim(rtrim(t_temp)));
    for (int t_itr = 0; t_itr < t; t_itr++) {
        string n_temp;
        getline(cin, n_temp);
        int n = stoi(ltrim(rtrim(n_temp)));
        string passwords_temp_temp;
        getline(cin, passwords_temp_temp);
        vector<string> passwords_temp = split(rtrim(passwords_temp_temp));
        vector<string> passwords(n);
        for (int i = 0; i < n; i++) {
            string passwords_item = passwords_temp[i];

            passwords[i] = passwords_item;
        }
        string loginAttempt;
        getline(cin, loginAttempt);
        string result = passwordCracker(passwords, loginAttempt);
        fout << result << "\n";
    }
    fout.close();
    return 0;
}

string ltrim(const string &str) {
    string s(str);
    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );
    return s;
}

string rtrim(const string &str) {
    string s(str);
    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );
    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;
    string::size_type start = 0;
    string::size_type end = 0;
    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }
    tokens.push_back(str.substr(start));
    return tokens;
}
