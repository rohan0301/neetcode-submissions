from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        same name diff email
        same email same name
        undirected graph each email will have associated emails. 
        neet@gmail.com, neet: [neet_dsa@gmail.com, bob@gmail.com]
        neet_dsa@gmail.com, neet: neet@gmail.com
        alice@gmail.com, alice: []
        bob@gmail.com, neet: [neet@gmail.com]
        neetcode@gmail.com, neet: []
        seen = set(neet@gmail.com)
        result = [[neet, neet@gmail.com, neet_dsa@gmail.com, bob@gmail.com]]
        first have alrexist = (False, None)
        loop through emails and if email already exists, then change to (True, email)
        then just add all the emails to that one that exists

        then do regular adj list where create an entry for each email and add the rest of the emails
        '''
        adj = defaultdict(list)
        for account in accounts:
            accExt = [False, None]
            for i in range(1, len(account)):
                if account[i] in adj:
                    accExt[0], accExt[1] = True, account[i]
            for i in range(1, len(account)):
                if accExt[0]:
                    adj[(accExt[1], account[0])].append(account[i])
                for j in range(1, len(account)):
                    #if i == j:
                     #   continue
                    adj[(account[i], account[0])].append(account[j])
        seen = set()
        result = []
        def dfs(email, name, emails):
            if email in seen:
                return
            seen.add(email)
            emails.append(email)
            for nxt in adj[(email,name)]:
                dfs(nxt,name,emails )
        
        for email, name in adj:
            if email not in seen:
                temp = []
                dfs(email, name, temp)
                temp.sort()
                result.append([name] + temp)
        return result

            
        #print(adj)


        