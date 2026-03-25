class Solution {
    private int answer = 0;
    
    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        
        dfs(k, 0, visited, dungeons);
        
        return answer;
    }
    
    private void dfs(Integer k, Integer count, boolean[] visited, int[][] dungeons) {
        answer = Math.max(count, answer);
        
        for (int i = 0; i < dungeons.length; i++) {
            if (!visited[i] && dungeons[i][0] <= k) {
                visited[i] = true;
                dfs(k - dungeons[i][1], count+1, visited, dungeons);
                visited[i] = false;
            }
        }
    }
}