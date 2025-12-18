**The Golden Rule:**

- Use Inheritance for **"Is-A" (A Dog is a Animal).**

- Use Composition for **"Has-A" (A Car has an Engine).**

In Composition, you simply create an object of one class inside another. This allows you to swap parts easily.

## 1. Why Composition is Powerful

Imagine you have a Report class. You want to export reports to PDF or HTML.

- **Inheritance Way:** PDFReport (Child), HTMLReport (Child).

- **Composition Way:** Report has an exporter attribute. You can switch from PDF to HTML at runtime without creating a new object.

---