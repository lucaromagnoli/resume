import os

from pylatex import Document, PageStyle, Head, MiniPage, NoEscape, LargeText, HugeText, LineBreak, MediumText, Foot, \
    Tabularx, \
    MultiColumn, TextColor, simple_page_number, Tabu, LongTabu, StandAloneGraphic, NewPage, NewLine, Command, HFill
from pylatex.utils import bold


def create_header(first_page: PageStyle) -> PageStyle:
    with first_page.create(Head("L"),) as header:
        header.append(HugeText(bold("Luca Romagnoli")))
        header.append(NewLine())
        header.append(MediumText(bold("Software Engineer")))
        header.append(NewLine())
        with header.create(
                Tabularx("X ", width_argument=NoEscape(r"\textwidth"))
        ) as header_table:
            header_table.add_row([MultiColumn(1, align='l', data=TextColor("blue", ''))])
            header_table.add_hline(color="blue")
    return first_page


def create_footer(first_page: PageStyle) -> PageStyle:
    with first_page.create(Foot("C")) as footer:
        with footer.create(Tabularx(
                "X X",
                width_argument=NoEscape(r"\textwidth"))) as footer_table:
            footer_table.add_row(
                [MultiColumn(2, align='l', data=TextColor("blue", ''))])
            footer_table.add_hline(color="blue")
            footer_table.add_empty_row()

            name = MiniPage(
                width=NoEscape(r"0.25\textwidth"),
                pos='t')
            name.append("Luca Romagnoli")

            page = MiniPage(width=NoEscape(r"0.25\textwidth"),
                                        pos='t', align='c')
            page.append(simple_page_number())

            footer_table.add_row([name, page])
    return first_page



def build_resume():
    geometry_options = {
        "head": "40pt",
        "margin": "0.5in",
        "bottom": "0.6in",
        "includeheadfoot": True
    }
    doc = Document(geometry_options=geometry_options)
    doc.preamble.append(NoEscape("\\renewcommand{\\familydefault}{\sfdefault}"))
    doc.preamble.append(Command('usepackage', 'helvet'))

    first_page = PageStyle("firstpage")
    first_page = create_header(first_page)
    first_page = create_footer(first_page)

    doc.preamble.append(first_page)

    # Add contact information
    with doc.create(Tabu("X[r]")) as contacts_table:
        contacts = MiniPage(width=NoEscape(r"0.49\textwidth"), pos='t!', align='r')
        contacts.append("Branch no.")
        contacts.append(LineBreak())
        contacts.append(bold("1181..."))
        contacts.append(LineBreak())
        contacts.append(bold("TIB Cheque"))

        contacts_table.add_row([contacts])
        contacts_table.add_empty_row()

    doc.change_document_style("firstpage")
    doc.add_color(name="lightgray", model="gray", description="0.80")

    doc.append(NewPage())

    # Add cheque images

    doc.generate_pdf("LucaRomagnoli_resume", clean_tex=False)



if __name__ == '__main__':
    build_resume()
