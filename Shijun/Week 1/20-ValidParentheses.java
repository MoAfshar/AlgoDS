class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> hashMap = new HashMap<> ();
        hashMap.put(')','(');
        hashMap.put(']','[');
        hashMap.put('}','{');
        
        Stack<Character> stack = new Stack<Character>();
        for (int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if (hashMap.containsValue(c)){  
                stack.push(c);
            } else if (!stack.isEmpty() && hashMap.containsKey(c) && hashMap.get(c)==stack.lastElement())
            //Don't need to check containsKey(c)
            {
                stack.pop();
            } else {
                return false;
            }
        }
        return stack.isEmpty();
    }
}