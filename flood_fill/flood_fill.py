def flood_fill(image, sr, sc, color):
    orig_color = image[sr][sc]
    if orig_color == color:
        return image

    def dfs(r, c):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != orig_color:
            return
        image[r][c] = color
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    dfs(sr, sc)
    return image