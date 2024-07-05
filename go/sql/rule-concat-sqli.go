// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42

package main

import (
	"context"
	"database/sql"
	"fmt"
	"strings"
)

func dbUnsafe(tainted string) {
	db, err := sql.Open("sqlite3", ":memory:")
	if err != nil {
		panic(err)
	}

	ctx := context.Background()

	unsafe1 := "select * from foo where bar = '" + tainted + "'"
	unsafe2 := "select * from foo where id = " + tainted
	unsafe3 := fmt.Sprintf("select * from foo where bar = %q", tainted)

	unsafe4 := strings.Builder{}
	unsafe4.WriteString("select * from foo where bar = ")
	unsafe4.WriteString(tainted)

	// ruleid:go_sql_rule-concat-sqli
	db.Exec(unsafe1)
	// ruleid:go_sql_rule-concat-sqli
	db.Exec(unsafe2)
	// ruleid:go_sql_rule-concat-sqli
	db.Exec(unsafe3)
	// ruleid:go_sql_rule-concat-sqli
	db.Exec(unsafe4.String())

	// ruleid:go_sql_rule-concat-sqli
	db.Exec("SELECT * FROM foo WHERE bar = '" + tainted + "'")
	// ruleid:go_sql_rule-concat-sqli
	db.ExecContext(ctx, "INSERT INTO foo VALUES('"+tainted+"')")
	// ruleid:go_sql_rule-concat-sqli
	db.Query("UPDATE foo SET bar = '" + tainted + "' WHERE id = 100")
	// ruleid:go_sql_rule-concat-sqli
	db.QueryContext(ctx, "select * from foo where bar = '"+tainted+"'")
	// ruleid:go_sql_rule-concat-sqli
	db.QueryRow("insert into foo values('" + tainted + "')")
	// ruleid:go_sql_rule-concat-sqli
	db.QueryRowContext(ctx, "update foo set bar = '"+tainted+"' where id = 100")
}

func dbSafe(tainted string) {
	db, err := sql.Open("sqlite3", ":memory:")
	if err != nil {
		panic(err)
	}

	ctx := context.Background()

	safe1 := "select * from foo where bar = '" + "safe" + "'"
	safe2 := "select * from foo where id = " + "safe"
	safe3 := fmt.Sprintf("select * from foo where bar = %q", "safe")

	// ok:go_sql_rule-concat-sqli
	db.Exec(safe1)
	// ok:go_sql_rule-concat-sqli
	db.Exec(safe2)
	// ok:go_sql_rule-concat-sqli
	db.Exec(safe3)

	// ok:go_sql_rule-concat-sqli
	db.Exec("SELECT * FROM foo WHERE bar = '" + "safe" + "'")
	// ok:go_sql_rule-concat-sqli
	db.ExecContext(ctx, "INSERT INTO foo VALUES('"+"safe"+"')")
	// ok:go_sql_rule-concat-sqli
	db.Query("UPDATE foo SET bar = '" + "safe" + "' WHERE id = 100")
	// ok:go_sql_rule-concat-sqli
	db.QueryContext(ctx, "select * from foo where bar = '"+"safe"+"'")
	// ok:go_sql_rule-concat-sqli
	db.QueryRow("insert into foo values('" + "safe" + "')")
	// ok:go_sql_rule-concat-sqli
	db.QueryRowContext(ctx, "update foo set bar = '"+"safe"+"' where id = 100")
}

func dbSafe2(tainted string) {
	db, err := sql.Open("sqlite3", ":memory:")
	if err != nil {
		panic(err)
	}

	ctx := context.Background()

	safe1 := "select * from foo where bar = ?"
	safe2 := "select * from foo where bar is $1 and baz = $2"

	// ok:go_sql_rule-concat-sqli
	db.Exec(safe1, tainted)
	// ok:go_sql_rule-concat-sqli
	db.Exec(safe2, true, tainted)

	// ok:go_sql_rule-concat-sqli
	db.Exec("SELECT * FROM foo WHERE bar = ?", tainted)
	// ok:go_sql_rule-concat-sqli
	db.ExecContext(ctx, "INSERT INTO foo VALUES(?)", tainted)
	// ok:go_sql_rule-concat-sqli
	db.Query("UPDATE foo SET bar = ? WHERE id = 100", tainted)
	// ok:go_sql_rule-concat-sqli
	db.QueryContext(ctx, "select * from foo where bar = ?", tainted)
	// ok:go_sql_rule-concat-sqli
	db.QueryRow("insert into foo values(?)", tainted)
	// ok:go_sql_rule-concat-sqli
	db.QueryRowContext(ctx, "update foo set bar = $2 and id = $1", "baz", tainted)
}

// False-positive reported by customer (see gitlab-org/gitlab#451108).
func safeIssue_451108(ctx context.Context, val string) error {
	if err := somepkg.validate(val); err != nil {
		return &somepkg.Error{Message: err.Error()}
	}

	if !updateAllowed(somepkg.Status) {
		// ok:go_sql_rule-concat-sqli
		return &somepkg.Error{Message: fmt.Sprintf("update is not permitted: %v", somepkg.Status)}
	}

	return nil
}
