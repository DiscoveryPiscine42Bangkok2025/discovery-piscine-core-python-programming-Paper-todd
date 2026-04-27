def checkmate(board: str):
    try:
        rows = board.splitlines()
        if not rows:
            return

        n = len(rows)
        for r in rows:
            if len(r) != n:
                return

        king = None
        for i in range(n):
            for j in range(n):
                if rows[i][j] == 'K':
                    if king is not None:
                        return
                    king = (i, j)

        if king is None:
            return

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < n

        def is_attacked(i, j):
            for x in range(n):
                for y in range(n):
                    if rows[x][y] == 'P':
                        if (x - 1, y - 1) == (i, j) or (x - 1, y + 1) == (i, j):
                            return True

            for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                x, y = i + di, j + dj
                while in_bounds(x, y):
                    if rows[x][y] != '.':
                        if rows[x][y] in ('R', 'Q'):
                            return True
                        break
                    x += di
                    y += dj

            for di, dj in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                x, y = i + di, j + dj
                while in_bounds(x, y):
                    if rows[x][y] != '.':
                        if rows[x][y] in ('B', 'Q'):
                            return True
                        break
                    x += di
                    y += dj

            return False

        ki, kj = king

        if not is_attacked(ki, kj):
            print("Fail")
            return

        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue

                ni, nj = ki + di, kj + dj
                if not in_bounds(ni, nj):
                    continue

                if rows[ni][nj] != '.':
                    continue

                if not is_attacked(ni, nj):
                    print("Fail")
                    return

        print("Success")

    except:
        return