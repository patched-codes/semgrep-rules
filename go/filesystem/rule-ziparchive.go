// License: Apache 2.0 (c) gosec
// source: https://github.com/securego/gosec/blob/master/testutils/source.go
// hash: bfb0f42

package main

import (
	"archive/tar"
	"archive/zip"
	"errors"
	"io"
	"os"
	"path"
	"path/filepath"
	"strings"
)

func unzip(archive, target string) error {
	reader, err := zip.OpenReader(archive)
	if err != nil {
		return err
	}

	if err := os.MkdirAll(target, 0750); err != nil {
		return err
	}

	for _, file := range reader.File {
		// ruleid:go_filesystem_rule-ziparchive
		path := filepath.Join(target, file.Name)
		if file.FileInfo().IsDir() {
			os.MkdirAll(path, file.Mode()) // #nosec
			continue
		}

		fileReader, err := file.Open()
		if err != nil {
			return err
		}
		defer fileReader.Close()

		targetFile, err := os.OpenFile(path, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, file.Mode())
		if err != nil {
			return err
		}
		defer targetFile.Close()

		if _, err := io.Copy(targetFile, fileReader); err != nil {
			return err
		}
	}

	return nil
}

func unzipIndirectFilename(archive, target string) error {
	reader, err := zip.OpenReader(archive)
	if err != nil {
		return err
	}

	if err := os.MkdirAll(target, 0750); err != nil {
		return err
	}

	for _, file := range reader.File {
		archiveFile := file.Name
		// ruleid:go_filesystem_rule-ziparchive
		path := filepath.Join(target, archiveFile)
		if file.FileInfo().IsDir() {
			os.MkdirAll(path, file.Mode()) // #nosec
			continue
		}

		fileReader, err := file.Open()
		if err != nil {
			return err
		}
		defer fileReader.Close()

		targetFile, err := os.OpenFile(path, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, file.Mode())
		if err != nil {
			return err
		}
		defer targetFile.Close()

		if _, err := io.Copy(targetFile, fileReader); err != nil {
			return err
		}
	}

	return nil
}

func safeExtract(f *zip.Reader, destPath string) error {
	if err := os.MkdirAll(destPath, 0750); err != nil {
		return err
	}

	for _, file := range f.File {
		archiveFile := file.Name
		// ok:go_filesystem_rule-ziparchive
		path := filepath.Clean(filepath.Join(destPath, archiveFile))
		if !strings.HasPrefix(path, destPath+string(filepath.Separator)) {
			return errors.New("Illegal path")
		}

		if file.FileInfo().IsDir() {
			os.MkdirAll(path, file.Mode()) // #nosec
			continue
		}

		fileReader, err := file.Open()
		if err != nil {
			return err
		}
		defer fileReader.Close()

		targetFile, err := os.OpenFile(path, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, file.Mode())
		if err != nil {
			return err
		}
		defer targetFile.Close()

		if _, err := io.Copy(targetFile, fileReader); err != nil {
			return err
		}
	}
	return nil
}

// f *zip.File: semgrep is not yet able to use params as sources
func extractFile(f *zip.File, destPath string) error {
	// ok:go_filesystem_rule-ziparchive
	filePath := path.Join(destPath, f.Name)
	os.MkdirAll(path.Dir(filePath), os.ModePerm)

	rc, err := f.Open()
	if err != nil {
		return err
	}
	defer rc.Close()

	fw, err := os.Create(filePath)
	if err != nil {
		return err
	}
	defer fw.Close()

	if _, err = io.Copy(fw, rc); err != nil {
		return err
	}

	if f.FileInfo().Mode()&os.ModeSymlink != 0 {
		return nil
	}

	if err = os.Chtimes(filePath, f.ModTime(), f.ModTime()); err != nil {
		return err
	}
	return os.Chmod(filePath, f.FileInfo().Mode())
}

func extractFileHeader(f *tar.Header, tr *tar.Reader, destPath string) error {
	// ok:go_filesystem_rule-ziparchive
	filePath := path.Join(destPath, f.Name)
	os.MkdirAll(path.Dir(filePath), os.ModePerm)

	fw, err := os.Create(filePath)
	if err != nil {
		return err
	}
	defer fw.Close()

	if _, err = io.Copy(fw, tr); err != nil {
		return err
	}

	if f.FileInfo().Mode()&os.ModeSymlink != 0 {
		return nil
	}

	if err = os.Chtimes(filePath, f.FileInfo().ModTime(), f.FileInfo().ModTime()); err != nil {
		return err
	}
	return os.Chmod(filePath, f.FileInfo().Mode())
}

