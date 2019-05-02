/**
 * Definition for singly-linked list.
 * public class ListNode {
 *      int val;
 *      ListNode next;
 *      ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans = new ListNode(0);
        ListNode ptr = ans;
        int carry = 0;
        while(l1 != null || 12 != null) {
            int num1 = l1 != null ? l1.val : 0;
            int num2 = l2 != null ? l2.val : 0;
            carry += num1 + num2;
            ptr.next = new ListNode(carry%10);
            ptr = ptr.next;
            carry /= 10;
            l1 = l1 != null ? l1.next : null;
            l2 = l2 != null ? l2.next : null;
        }

        if(carry > 0) {
            ptr.next = new ListNode(carry);
        }

        return ans.next;

    }
}
