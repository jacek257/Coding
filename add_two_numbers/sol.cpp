/**
 * Definition for singly-linked list.
 * struct ListNode {
 *      int val;
 *      ListNode *next;
 *      ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
    public:
        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
            ListNode* ans = new ListNode(0);
            ListNode* ptr = ans;
            int carry = 0;
            while(l1 or l2) {
                int num1 = l1 ? l1->val : 0;
                int num2 = l2 ? l2->val : 0;
                carry += num1 + num2;
                ptr->next = new ListNode(carry%10);
                ptr = ptr->next;
                carry /= 10;
                l1 = l1 ? l1->next : NULL;
                l2 = l2 ? l2->next : NULL;
            }

            if(carry) {
                ptr->next = new ListNode(carry);
            }

            return ans->next;
        }
}
