"""
Given a list of accounts where each element accounts[i] is a list of strings,
where the first element accounts[i][0] is a name,
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts.
Two accounts definitely belong to the same person if there is some common email to both accounts.
Note that even if two accounts have the same name,
they may belong to different people as people could have the same name.
A person can have any number of accounts initially,
but all of their accounts definitely have the same name.

After merging the accounts,
return the accounts in the following format:
the first element of each account is the name,
and the rest of the elements are emails in sorted order.
The accounts themselves can be returned in any order.



Example 1:
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                   ["John","johnsmith@mail.com","john00@mail.com"],
                   ["Mary","mary@mail.com"],
                   ["John","johnnybravo@mail.com"]]

Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]]

Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer
[['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Example 2:
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
                   ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
                   ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
                   ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
                   ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]

Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
         ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
         ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
         ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
         ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]


Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email."""

from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        no_accounts = len(accounts)
        int2account: dict[int, str] = {i: account[0] for i, account in enumerate(accounts)}
        self.parents = [i for i in range(no_accounts)]
        self.count = no_accounts

        self.size = [len(account) for account in accounts]

        for i in range(0, no_accounts - 1):  # left
            for j in range(i + 1, no_accounts):  # right
                left = accounts[i]
                right = accounts[j]

                if self.is_connected(left[1:], right[1:]):
                    self.union(i, j)  # Connect the accounts

        for i in range(no_accounts):
            self.parents[i] = self.find(i)

        roots = set(self.parents)
        outputs = [[int2account[i]] for i in range(no_accounts)]
        # rebuild

        for i, parent in enumerate(self.parents):
            if i not in roots:
                # This got merged in with a different user
                # Add emails to parent
                for email in accounts[i][1:]:
                    if email not in outputs[parent]:
                        outputs[parent].append(email)
            else:
                for email in accounts[i][1:]:
                    if email not in outputs[i]:
                        outputs[i].append(email)

        filtered_output = []

        for output in outputs:
            new_filtered_row = []
            if len(output) <= 1:
                continue
            new_filtered_row.append(output[0])
            new_filtered_row.extend(sorted(output[1:]))
            filtered_output.append(new_filtered_row)

        return filtered_output

    def is_connected(self, left: list[str], right: list[str]) -> bool:

        for email in left:
            for other in right:
                if email == other:
                    return True

        return False

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a: int, b: int) -> bool:

        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False  # already union

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parents[rb] = ra
        self.size[ra] += self.size[rb]
        self.count -= 1
        return True


accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]

mySolution = Solution()
print(mySolution.accountsMerge(accounts))
