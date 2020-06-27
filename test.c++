void DslktoFile(Dslk& l, char* file)
{
	std::fstream f;
	f.open(file, std::ios::out | std::ios::binary);
	Node* n = l.head;
	while (f.write(reinterpret_cast<char*>(&(n->Sach)), sizeof(Thuvien))&&n)
		n = n->pNext;
	f.close();
	Node* i = l.head;
	//Giải phóng vùng nhớ dslk
	while (l.head != NULL)
	{
		i = l.head;
		l.head = i->pNext;
		delete i;
	}
	l.head = l.tail = NULL;
}