#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lastSeeCharPos = {}
        maxLen = 0
        start = 0
        for i in range(len(s)):
            c = s[i]
            # 在(start,i] 发现重复字母,在上一次重复位置继续查找
            # start不需要从0-len以1位单位递增
            '''
                a9876bcd123cbd
                s     x    p 
                若从s+1开始,最大长度为p-(s+1),必然小于p-s,必须从x+1位置开始才有可能产生大于p-s的长度
            '''
            if c in lastSeeCharPos and lastSeeCharPos[c] >= start:
                start = lastSeeCharPos[c] + 1
            else:
                maxLen = max(maxLen, i - start + 1)
            lastSeeCharPos[c] = i
        return maxLen
        """
        :type s: str
        :rtype: int
        """


print Solution().lengthOfLongestSubstring("abcabcbb")