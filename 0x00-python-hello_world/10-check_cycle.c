#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - search for a loop
 * @list: linked list
 * Return: 0 no cycle 1 cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp, *tmp2;

	tmp = list;
	while (tmp->next)
	{
		tmp2 = list;
		while (tmp2 != tmp)
		{
			if (tmp->next == tmp2)
				return (1);
			tmp2 = tmp2->next;
		}
		tmp = tmp->next;
	}
	return (0);
}
