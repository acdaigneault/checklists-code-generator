## Generate Latex code for list material

list_filename = "avionics_recovery_material.txt"
code_filename = "code_" + list_filename


with open(list_filename) as f:
    items = f.read().split("\n")

# check if odd or even
n_items = len(items)
if n_items % 2 == 0:
    half = int(n_items/2)
    left_items =  items[:half]
    right_items = items[half:]
else:
    half = int((n_items+1)/2)
    left_items =  items[:half]
    right_items = items[half:]
    right_items.append(" ")

with open(code_filename, "w") as file:
    file.write("\\begin{center}\n")
    file.write("    \\begin{tabular}{|m{0.05\paperwidth} m{0.71\paperwidth}|m{0.015\paperwidth}|}\n")
    file.write(f"        \hline \listTitle & \large\\bf  & \\\\ \n")
    file.write("        \hline \listElem & Prepare the material : & \cellcolor{Black} \\\\\n")
    file.write("    \hline\end{tabular}\n\n")
    file.write("    \\vspace{-1.5pt}\n")
    file.write("% Write material list here (or use .txt file and Python code)\n")
    file.write("    \\begin{minipage}{0.415\paperwidth}\n")
    file.write("        \\begin{tabular}{|m{0.05\paperwidth} m{0.29\paperwidth}|m{0.015\paperwidth}|}\n")


    for i in range(len(left_items)):
        if i == 0:
            file.write(f"                    \subListElem & \hspace{{5pt}}  {left_items[i]} &  \\\\\n")
        else:
            file.write(f"            \hline  \subListElem & \hspace{{5pt}}  {left_items[i]} &  \\\\ \n")

    file.write("            \hline\end{tabular} \n")
    file.write("    \\end{minipage}%\n")
    file.write("    \\begin{minipage}{0.45\paperwidth} \n")
    file.write("        \\begin{tabular}{m{0.05\paperwidth} m{0.2957\paperwidth}|m{0.015\paperwidth}|} \n")

    for i in range(len(right_items)):
        if i == 0:
            file.write(f"                    \subListElem & \hspace{{5pt}}  {right_items[i]} &  \\\\ \n")
        else:
            file.write(f"            \hline  \subListElem & \hspace{{5pt}}  {right_items[i]} &  \\\\ \n")

    file.write("        \hline \end{tabular} \n")
    file.write("    \end{minipage} \n")
    file.write("\\begin{tabular}{ |m{0.05\paperwidth} m{0.71\paperwidth}|m{0.015\paperwidth}| } \n")
    file.write("% Write checklist's steps here \n")
    file.write("   \listElem &  & \\\\ \n")

    file.write("\hline\end{tabular} \n")
    file.write("\end{center}  \n")
    file.write("\smallskip \n")

