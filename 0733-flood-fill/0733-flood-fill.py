class Solution(object):
    def floodFill(self, image, sr, sc, color):
        origin_color = image[sr][sc]
        image[sr][sc] = color

        if sr - 1 >= 0 and image[sr-1][sc] == origin_color and color != origin_color:
            self.floodFill(image, sr-1, sc, color)
        if sr + 1 < len(image) and image[sr+1][sc] == origin_color and color != origin_color:
            self.floodFill(image, sr+1, sc, color)
        if sc - 1 >= 0 and image[sr][sc-1] == origin_color and color != origin_color:
            self.floodFill(image, sr, sc-1, color)
        if sc + 1 < len(image[0]) and image[sr][sc+1] == origin_color and color != origin_color:
            self.floodFill(image, sr, sc+1, color)

        return image