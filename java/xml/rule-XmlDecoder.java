// License: MIT (c) GitLab Inc.
package xml;

import java.io.*;
import java.beans.XMLDecoder;
import java.util.ArrayList;
import java.util.List;

class TestXmlDecoder {

    String safeVariable = "";

    // This will just create a file in your /tmp/ folder named Hacked1.txt
    void decodeObjectUnsafe1() throws IOException {
        InputStream inputStream = TestXmlDecoder.class.getClassLoader()
                .getResourceAsStream("xmldecoder-rce.xml");
        XMLDecoder decoder = new XMLDecoder(inputStream);
        // ruleid: java_xml_rule-XmlDecoder
        Object o = decoder.readObject();
        decoder.close();
        System.out.println("Check your /tmp/ folder for Hacked1.txt file");
    }

    // This will just create a file in your /tmp/ folder named Hacked2.txt
    void decodeObjectUnsafe2() throws IOException {
        ClassLoader customClassLoader = null;
        InputStream inputStream = TestXmlDecoder.class.getClassLoader()
                .getResourceAsStream("xmldecoder-rce2.xml");

        XMLDecoder decoder = new XMLDecoder(inputStream,
                null,
                exception -> {
                    System.err.println("Exception occurred: " + exception.getMessage());
                },
                customClassLoader);
        // ruleid: java_xml_rule-XmlDecoder
        Object o = decoder.readObject();
        decoder.close();
        System.out.println("Check your /tmp/ folder for Hacked2.txt file");
    }

    void decodeObjectUnsafe3() throws IOException {
        System.out.println("Running Unsafe3(): (Unsafe ClassLoader implementation)");
        ClassLoader customClassLoader = new ClassLoader() {
            @Override
            protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                return super.loadClass(name, resolve);
            }
        };

        InputStream inputStream = TestXmlDecoder.class.getClassLoader()
                .getResourceAsStream("xmldecoder-rce2.xml");

        try {
            XMLDecoder decoder = new XMLDecoder(inputStream,
                    null,
                    exception -> {
                        System.err.println("Exception occurred: " + exception.getMessage());
                    },
                    customClassLoader);
            // ruleid: java_xml_rule-XmlDecoder
            Object o = decoder.readObject();
            decoder.close();
        } catch (Exception e) {
            System.err.println("Exception occurred: " + e.getMessage());
        }
    }

    void decodeObjectUnsafe4() throws IOException {
        System.out.println("Running Unsafe4(): (Unsafe ClassLoader implementation)");
        ClassLoader customClassLoader = new ClassLoader() {
            @Override
            protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                if (!name.equals(
                        TestXmlDecoder.class.getName()) &&
                        !name.equals(XMLDecoder.class.getName())) {

                    return super.loadClass(name, resolve);
                }
                return super.loadClass(name, resolve);
            }
        };

        InputStream inputStream = TestXmlDecoder.class.getClassLoader()
                .getResourceAsStream("xmldecoder-rce2.xml");

        try {
            XMLDecoder decoder = new XMLDecoder(inputStream,
                    null,
                    exception -> {
                        System.err.println("Exception occurred: " + exception.getMessage());
                    },
                    customClassLoader);
            // ruleid: java_xml_rule-XmlDecoder
            Object o = decoder.readObject();
            decoder.close();
        } catch (Exception e) {
            System.err.println("Exception occurred: " + e.getMessage());
        }
    }

    void decodeObjectUnsafe5() throws IOException {
        System.out.println("Running Unsafe5(): (Unsafe ClassLoader implementation)");

        InputStream inputStream = TestXmlDecoder.class.getClassLoader()
                .getResourceAsStream("xmldecoder-rce2.xml");

        try {
            XMLDecoder decoder = new XMLDecoder(inputStream,
                    null,
                    exception -> {
                        System.err.println("Exception occurred: " + exception.getMessage());
                    },
                    new ClassLoader() {
                        @Override
                        protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                            return super.loadClass(name, resolve);
                        }
                    });
            // ruleid: java_xml_rule-XmlDecoder
            Object o = decoder.readObject();
            decoder.close();
        } catch (Exception e) {
            System.err.println("Exception occurred: " + e.getMessage());
        }
    }

    void decodeObjectUnsafe6() throws IOException {
        System.out.println("Running Unsafe6(): (Unsafe ClassLoader implementation)");

        InputStream inputStream = TestXmlDecoder.class.getClassLoader()
                .getResourceAsStream("xmldecoder-rce2.xml");

        try {
            XMLDecoder decoder = new XMLDecoder(inputStream,
                    null,
                    exception -> {
                        System.err.println("Exception occurred: " + exception.getMessage());
                    },
                    new ClassLoader() {
                        @Override
                        protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                            if (!name.equals(
                                    TestXmlDecoder.class.getName()) &&
                                    !name.equals(XMLDecoder.class.getName())) {

                                return super.loadClass(name, resolve);
                            }
                            return super.loadClass(name, resolve);
                        }
                    });
            // ruleid: java_xml_rule-XmlDecoder
            Object o = decoder.readObject();
            decoder.close();
        } catch (Exception e) {
            System.err.println("Exception occurred: " + e.getMessage());
        }
    }

    void decodeObjectSafe1() throws IOException {
        System.out.println("Running Safe1(): (Exceptions will be thrown)");
        ClassLoader customClassLoader = new ClassLoader() {
            @Override
            protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                if (!name.equals(
                        TestXmlDecoder.class.getName()) &&
                        !name.equals(XMLDecoder.class.getName())) {
                    throw new RuntimeException("Unauthorized deserialization attempt: " + name);
                }
                return super.loadClass(name, resolve);
            }
        };

        InputStream inputStream = TestXmlDecoder.class.getClassLoader()
                .getResourceAsStream("xmldecoder-rce2.xml");

        try {
            XMLDecoder decoder = new XMLDecoder(inputStream,
                    null,
                    exception -> {
                        System.err.println("Exception occurred: " + exception.getMessage());
                    },
                    customClassLoader);
            // ok: java_xml_rule-XmlDecoder
            Object o = decoder.readObject();
            decoder.close();
        } catch (Exception e) {
            System.err.println("Exception occurred: " + e.getMessage());
        }
    }

    void decodeObjectSafe2() throws IOException {
        System.out
                .println("Running Safe2(): (This should run normally as xml file does not contain malicious payload.)");

        InputStream inputStream = TestXmlDecoder.class.getClassLoader()
                .getResourceAsStream("xmldecoder-safe.xml");

        XMLDecoder decoder = new XMLDecoder(inputStream,
                null,
                exception -> {
                    System.err.println("Exception occurred: " + exception.getMessage());
                },
                new ClassLoader() {
                    @Override
                    protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                        if (!name.equals(
                                TestXmlDecoder.class.getName()) &&
                                !name.equals(XMLDecoder.class.getName())) {
                            throw new RuntimeException("Unauthorized deserialization attempt: " + name);
                        }
                        return super.loadClass(name, resolve);
                    }
                });
        // ok: java_xml_rule-XmlDecoder
        Object o = decoder.readObject();
        decoder.close();
    }

    void decodeObjectSafe3() throws IOException {
        List<String> allowedClasses = new ArrayList<>();
        allowedClasses.add(TestXmlDecoder.class.getName());
        allowedClasses.add(XMLDecoder.class.getName());

        System.out.println("Running Safe3(): (Exceptions will be thrown)");
        ClassLoader customClassLoader = new ClassLoader() {
            @Override
            protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                if (!allowedClasses.contains(name)) {
                    throw new RuntimeException("Unauthorized deserialization attempt: " + name);
                }
                return super.loadClass(name, resolve);
            }
        };

        InputStream inputStream = TestXmlDecoder.class.getClassLoader()
                .getResourceAsStream("xmldecoder-rce2.xml");

        try {
            XMLDecoder decoder = new XMLDecoder(inputStream,
                    null,
                    exception -> {
                        System.err.println("Exception occurred: " + exception.getMessage());
                    },
                    customClassLoader);
            // ok: java_xml_rule-XmlDecoder
            Object o = decoder.readObject();
            decoder.close();
        } catch (Exception e) {
            System.err.println("Exception occurred: " + e.getMessage());
        }
    }

    void decodeObjectSafe4() throws IOException {
        List<String> allowedClasses = new ArrayList<>();
        allowedClasses.add(TestXmlDecoder.class.getName());
        allowedClasses.add(XMLDecoder.class.getName());

        System.out.println("Running Safe4(): (Exceptions will be thrown)");

        InputStream inputStream = TestXmlDecoder.class.getClassLoader()
                .getResourceAsStream("xmldecoder-rce2.xml");

        try {
            XMLDecoder decoder = new XMLDecoder(inputStream,
                    null,
                    exception -> {
                        System.err.println("Exception occurred: " + exception.getMessage());
                    },
                    new ClassLoader() {
                        @Override
                        protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
                            if (!allowedClasses.contains(name)) {
                                throw new RuntimeException("Unauthorized deserialization attempt: " + name);
                            }
                            return super.loadClass(name, resolve);
                        }
                    });
            // ok: java_xml_rule-XmlDecoder
            Object o = decoder.readObject();
            decoder.close();
        } catch (Exception e) {
            System.err.println("Exception occurred: " + e.getMessage());
        }
    }

    public void setSafeVariable(String str) {
        safeVariable = str;
        System.out.println("SafeVariable set: " + safeVariable);
    }

}
