import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        
        HashMap<String, Integer> total = new HashMap<>();
        HashMap<String, List<int[]>> genrePlay = new HashMap<>();
        
        for (int i = 0; i < genres.length; i++) {
            // 장르별로 재생 횟수 더하기
            if (total.containsKey(genres[i])) {
                total.put(genres[i], total.get(genres[i]) + plays[i]);
            } else {
                total.put(genres[i], plays[i]);
            }
            
            // genrePlay에 "장르: 인덱스, 재생 횟수" 저장하기
            genrePlay.putIfAbsent(genres[i], new ArrayList<>());
            genrePlay.get(genres[i]).add(new int[]{i, plays[i]});
        }
        
        // 재생 횟수를 기준으로 내림차순 정렬
        List<String> sortedGenre = new ArrayList<>(total.keySet());
        sortedGenre.sort((a, b) -> total.get(b).compareTo(total.get(a)));
        
        for (String genre: sortedGenre) {
            List<int[]> song = genrePlay.get(genre);
            
            // 고유 번호를 기준으로 내림차순 정렬 (재생횟수가 같으면 고유번호 빠른 순으로)
            song.sort((a, b) -> {
                if (a[1] == b[1]) return a[0] - b[0];
                return b[1] - a[1];
            });
            
            // 출력값에 최대 2개까지만 담기
            answer.add(song.get(0)[0]);
            if (song.size() > 1) {
                answer.add(song.get(1)[0]);
            }
        }
        
        int[] ans = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            ans[i] = answer.get(i);
        }
        
        return ans;
    }
}